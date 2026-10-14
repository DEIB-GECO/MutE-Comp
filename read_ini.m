function value = getIniValue(iniFilePath, varName)
    % Function to extract the value of a variable from an INI file
    % and resolve extended interpolation.
    %
    % iniFilePath: Path to the INI file
    % varName: Name of the variable to extract
    
    % Read INI file
    iniData = readIniFile(iniFilePath);
    
    % Check if the variable exists
    if isfield(iniData, varName)
        value = iniData.(varName);
        
        % Resolve extended interpolation
        value = resolveInterpolation(value, iniData);
    else
        error('Variable "%s" not found in INI file.', varName);
    end
end

function iniData = readIniFile(iniFilePath)
    % Helper function to read an INI file and return a struct
    % This assumes a simple INI file with key-value pairs and no sections.
    
    fid = fopen(iniFilePath, 'r');
    iniData = struct();
    
    while ~feof(fid)
        line = strtrim(fgets(fid));
        
        % Ignore empty lines and comments
        if isempty(line) || startsWith(line, ';') || startsWith(line, '#')
            continue;
        end
        
        % Parse key-value pair
        tokens = regexp(line, '^(.*?)\s*=\s*(.*)$', 'tokens');
        if ~isempty(tokens)
            key = strtrim(tokens{1}{1});
            value = strtrim(tokens{1}{2});
            iniData.(key) = value;
        end
    end
    
    fclose(fid);
end

function value = resolveInterpolation(value, iniData)
    % Helper function to resolve extended interpolation using other variables
    pattern = '\$\{([a-zA-Z0-9_]+)\}';
    
    % Use regular expressions to find patterns like ${varName}
    while true
        match = regexp(value, pattern, 'tokens', 'once');
        if isempty(match)
            break; % No more interpolation to resolve
        end
        
        interpVarName = match{1};
        
        % Check if the interpolated variable exists in iniData
        if isfield(iniData, interpVarName)
            % Replace the interpolation pattern with the actual value
            value = strrep(value, ['${' interpVarName '}'], iniData.(interpVarName));
        else
            error('Interpolated variable "%s" not found.', interpVarName);
        end
    end
end
