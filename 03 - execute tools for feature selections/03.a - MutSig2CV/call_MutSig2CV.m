% 04.a.1 - MutSig2CV
% invalid Matlab file name

path_mutsig = "/mnt/Data/_ThesisEX/programs/MutSig2CV/src";
path_repo = "/mnt/Data/_ThesisEX/RAS-CRC_analysis/";

cd("../../")

input = path_repo + read_ini("data.ini", "mutsig___all_noHypoHyper___in");
output = path_repo + read_ini("data.ini", "mutsig___all_noHypoHyper___out_dir");

input_RAS = path_repo + read_ini("data.ini", "mutsig___all_noHypoHyper_RAS___in");
output_RAS = path_repo + read_ini("data.ini", "mutsig___all_noHypoHyper_RAS___out_dir");

input_nonRAS = path_repo + read_ini("data.ini", "mutsig___all_noHypoHyper_nonRAS___in");
output_nonRAS = path_repo + read_ini("data.ini", "mutsig___all_noHypoHyper_nonRAS___out_dir");

cd(path_mutsig);

MutSig2CV(char(input), char(output));
MutSig2CV(char(input_RAS), char(output_RAS));
MutSig2CV(char(input_nonRAS), char(output_nonRAS));
