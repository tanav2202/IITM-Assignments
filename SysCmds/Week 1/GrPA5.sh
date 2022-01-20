read var1
mkdir dir_1 dir_2
touch dir_1/file_1
touch dir_1/file_$var1
touch dir_1/file_3

mv ./dir_1/file_1 dir_2;
rm -rf dir_1