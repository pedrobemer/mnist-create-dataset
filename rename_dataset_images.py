import os 
import csv

path = "/home/pedrobemer/Git/mnist_png/mnist_png"
new_path = "/home/pedrobemer/Git/mnist-create-dataset/mnist_png"
os.mkdir(new_path)

# create the csv writer
result = os.path.exists('/home/pedrobemer/Git/mnist-create-dataset/mnist_database.csv')

# if not result:
f = open('/home/pedrobemer/Git/mnist-create-dataset/mnist_database.csv', 'w')
writer = csv.writer(f)

header_row = ["id", "label", "purpose", "s3Location"]
# write a row to the csv file
writer.writerow(header_row)

# close the file
f.close()

dir_list = os.listdir(path)
print(dir_list)

idx = 0
for dir in dir_list:
    os.mkdir(new_path + "/" + dir)
    inside_dir_list = os.listdir(path + "/" + dir)
    for label in inside_dir_list:
        os.mkdir(new_path + "/" + dir + "/" + label)
        label_path = path + "/" + dir + "/" + label
        label_images_files = os.listdir(label_path)
        for images in label_images_files:

                s3_location = "s3://bucket_location/mnist/" + \
                    dir + "/" + label + "-" + images
                new_img_name = label + "-" + images
                new_img_path = new_path + "/" + dir + "/" + label + "/" + new_img_name
                os.rename(label_path + "/" + images, new_img_path)
                # write a row to the csv file
                idx += 1
