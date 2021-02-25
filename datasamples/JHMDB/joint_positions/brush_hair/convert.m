


CurrentFolder=pwd;
AllFile=dir('.');
FolderOnly=AllFile([AllFile.isdir]);


for k=3:length(FolderOnly)
  disp(FolderOnly(k).name);
  d=load(strcat(FolderOnly(k).name,'/joint_positions.mat'));
  csvwrite(strcat(FolderOnly(k).name,'/pos_img.csv'),d.pos_img);
  csvwrite(strcat(FolderOnly(k).name,'/pos_world.csv'),d.pos_world);
  csvwrite(strcat(FolderOnly(k).name,'/scale.csv'),d.scale);
end
