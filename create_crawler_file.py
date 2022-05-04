import os 
import csv

path = "/home/pedrobemer/Git/mnist_png/mnist_png"

dir_list = os.listdir(path)
print(dir_list)

idx = 0
with open('/home/pedrobemer/Git/mnist-create-dataset/mnist_database.csv', 'w') as f:
    header_row = ["id", "label", "purpose", "s3Location"]

    # create the csv writer
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header_row)
    for dir in dir_list:
        inside_dir_list = os.listdir(path + "/" + dir)

        for label in inside_dir_list:
            label_images_files = os.listdir(path + "/" + dir + "/" + label)
            for images in label_images_files:

                    s3_location = "s3://bucket_location/mnist/" + \
                        dir + "/" + label + "-" + images
                    row = [idx, label, dir, s3_location]
                    print(row)
                    # write a row to the csv file
                    writer.writerow(row)
                    idx += 1
