__author__ = 'Abhishek'
import csv
import sys
import getopt
def business_extractor(businesscsvfile,category_name):
    business_categories = list()
    restaurant_businesses = list()
    with open(businesscsvfile,"rU") as csvfile:
        businessreader = csv.reader(csvfile)
        for row in businessreader:
            business_categories.append(row)
    a = "abhishek"
    for eachitem in business_categories:
        if(eachitem[9].find(category_name,0,len(eachitem[9]))!= -1):
            restaurant_businesses.append(eachitem[16])
    return restaurant_businesses

def review_extractor(reviewcsvfile,business_list):
    review_list = []
    with open(reviewcsvfile,"rU") as csvfile:
        reviewreader = csv.reader(csvfile)
        for row in reviewreader:
            if row[4] in business_list:
                temp_list = []
                temp_list.append(row[0])
                temp_list.append(row[1])
                temp_list.append(row[2])
                temp_list.append(row[6])
                review_list.append(temp_list)
    return review_list
def extract_ratingwise_reviews(reviews):
    rating1 = []
    rating2 = []
    rating3 = []
    rating4 = []
    rating5 = []
    for each_review in reviews:
        if each_review[3] is '1':
            rating1.append(each_review)
        elif each_review[3] is '2':
            rating2.append(each_review)
        elif each_review[3] is '3':
            rating3.append(each_review)
        elif each_review[3] is '4':
            rating4.append(each_review)
        elif each_review[3] is '5':
            rating5.append(each_review)
    return [rating1,rating2,rating3,rating4,rating5]


def main(argv):
    #Enter the arguments in the order businesscsvfile,category_name,reviewcsvfile
    businesscsvfile = argv[0]
    category_name = argv[1]
    reviewcsvfile = argv[2]

    category_businesses = business_extractor(businesscsvfile,category_name)
    reviews = review_extractor(reviewcsvfile, category_businesses)
    rating_list = extract_ratingwise_reviews(reviews)
    training = []
    validate = []
    test = []
    for each_ratinglist in rating_list:
        #print (str)(len(each_ratinglist))+"\n"
        validate_border = (int)(0.2 * len(each_ratinglist))
        #print (str)(validate_border) +"\n"
        test_border = (int)(0.5 * validate_border)
        #print (str)(test_border) + "\n"
        for i in range(0,test_border):
            test.append(each_ratinglist[i])
        for j in range(test_border,validate_border):
            validate.append(each_ratinglist[j])
        for k in range(validate_border,len(each_ratinglist)):
            training.append(each_ratinglist[k])
    with open(category_name+"training.csv", "wb") as trainingfile:
        writer = csv.writer(trainingfile)
        writer.writerows(training)
    with open(category_name+"validate.csv", "wb") as validatefile:
        writer = csv.writer(validatefile)
        writer.writerows(validate)
    with open(category_name+"test.csv", "wb") as testfile:
        writer = csv.writer(testfile)
        writer.writerows(test)






    #reviews has user,business,star,reviewid,reviewtext and star
if __name__ == "__main__":
    #Enter the arguments in the order businesscsvfile,category_name,reviewcsvfile
    main(sys.argv[1:])

