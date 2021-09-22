from pymongo import MongoClient
from bson.son import SON
def test(x):
    myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('root', 'root'))
    mydb = myclient['test1']
    collection = mydb['student']
    if x==1:
        # record = {
        #     "user": "raj",
        #     "roll_number": 101,
        #     "branch": "cse",
        #     "marks": 40
        #     }
        # record_1 = collection.insert_one(record)
        # mylist = [
        #            {
        #                           "_id": 19,
        #                           "name": "john",
        #                           "roll_number": 103,
        #                           "branch": "cse",
        #                           "marks": 45
        #                       },
        #            {
        #             "_id": 20,
        #             "name": "jenny",
        #             "roll_number": 108,
        #             "branch": "cse",
        #             "marks": 55
        #         },
        #             {
        #                 "_id": 21,
        #                 "name": "joe",
        #                 "roll_number": 105,
        #                 "branch": "cse",
        #                 "marks": 55
        #             },
        #     {
        #         "_id": 10,
        #         "name": "jenny",
        #         "roll_number": 108,
        #         "branch": "cse",
        #         "marks": 55
        #     }
        #
        #         ]
        mylist = [
            {"x": 1, "tags": ['cat', 'dog']},
            {"x": 2, "tags": ['cat']},
            {"x": 3, "tags": ['cat', 'dog', 'lion']},
            {"x": 4, "tags": ['cat', 'dog']},
            {"x": 5, "tags": []},
        ]
        collection.insert_many(mylist)

        return 'inserted Successfully'
    elif x==2:
        all_document = collection.find()
        for each_record in all_document:
            print("doc", each_record)
        return 'Display Successfully'
    elif x==3:
        agg_result = collection.aggregate([{
            "$group": {
                "_id": "$name",
                "num_lang": {"$sum": 1}
            }}
        ])
        print(agg_result)
        pipeline = [
            {
                "$unwind":"$tags"
            },
            {
                "$group":{"_id": "$tags", "count": {"$sum": 1}}
            },
            {
                "$sort": SON([('count', -1), ('_id', -1)])
            }
        ]
        agg_result = collection.aggregate(pipeline)
        for i in agg_result:
            print(i)


while True:
    print('1.Create a document')
    print('2.Display document')
    print('3.Aggregate document')
    print('4.End the process')
    print("Enter your Choice: ")
    x = int(input())
    if x == 1 or x == 2 or x == 3:
        print(test(x))
    else:
        break
