CurrentFolder = pwd;
AllFile=dir(fullfile(CurrentFolder,'F*'));
FolderOnly=AllFile([AllFile.isdir]);


for k=1:length(FolderOnly)
  load(strcat(FolderOnly{k},'/joint_positions.mat'))
  csvwrite(strcat(FolderOnly{k},'/pos_img.csv'),pos_img)
  csvwrite(strcat(FolderOnly{k},'/pos_world.csv'),pos_world)
  csvwrite(strcat(FolderOnly{k},'/scale.csv'),scale)
end
