# You will need the 'ini' package to read INI files.
# Install the package if you don't have it already:
# install.packages("ini")

library(ini)

# Function to get value of a variable from INI file with extended interpolation
get_ini_value <- function(ini_file_path, var_name) {
  # Read the INI file
  ini_data <- read.ini(ini_file_path)

  # Flatten the sections into a single list for easier access
  ini_data_flat <- unlist(ini_data)

  # remove the section names from the variable names
  names(ini_data_flat) <- gsub(".*\\.", "", names(ini_data_flat))

  # Check if the variable exists
  if (!var_name %in% names(ini_data_flat)) {
    stop(paste("Variable", var_name, "not found in INI file."))
  }

  # Get the value of the variable
  value <- ini_data_flat[[var_name]]

  # Resolve extended interpolation
  value <- resolve_interpolation(value, ini_data_flat)

  return(value)
}

# Helper function to resolve interpolation
resolve_interpolation <- function(value, ini_data_flat) {
  pattern <- "\\$\\{([a-zA-Z0-9_]+)\\}" # Regular expression to match ${varName}

  # Use a while loop to repeatedly resolve interpolation
  while (grepl(pattern, value)) {
    # Find the variable inside ${}
    var_match <- regmatches(value, regexec(pattern, value))[[1]]

    if (length(var_match) > 1) {
      interp_var_name <- var_match[2] # The variable name inside ${}

      # Check if the interpolated variable exists
      if (!interp_var_name %in% names(ini_data_flat)) {
        stop(paste("Interpolated variable",
                    interp_var_name,
                   "not found in INI file."))
      }

      # Replace the interpolation with the actual value
      interp_value <- ini_data_flat[[interp_var_name]]
      value <- sub(pattern, interp_value, value, fixed = FALSE)
    }
  }

  return(value)
}
