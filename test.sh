echo "Enter the original picture name:"
read original_picture
echo "Enter the result picture name:"
read result_picture
echo "Please input the length of window:"
read length
echo './picture/'$original_picture
echo $length
echo './picture/multi'$original_picture
python flair_sliding_window.py './picture/'$original_picture $length './picture/multi'$original_picture








