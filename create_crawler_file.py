import os 
import csv

path = "/home/pedrobemer/Git/mnist_png/mnist_png"

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
with open('/home/pedrobemer/Git/mnist-create-dataset/mnist_database.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f, delimiter=',')
    for dir in dir_list:
        inside_dir_list = os.listdir(path + "/" + dir)

        for label in inside_dir_list:
            label_images_files = os.listdir(path + "/" + dir + "/" + label)
            for images in label_images_files:

                    s3_location = "s3://itau-corp-raw-us-east-1-360578360405/mnist/" + \
                        dir + "/" + label + "-" + images
                    row = [idx, label, dir, s3_location]
                    print(row)
                    # write a row to the csv file
                    writer.writerow(row)
                    idx += 1
