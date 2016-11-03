clear all
cnn = load('cnn.mat');



picture = load('50pictures93.mat');

picture_data = picture.data;
test_x = double(reshape(picture_data',50,50,36100))/255;

result = cnnff(cnn.cnn, test_x);
output = result.o;
save('/Users/wangzhe/Desktop/CNN/test/50output93.mat','output')

