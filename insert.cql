# Insert.cql
#
# By: Jeff Davies
#
# Create some data in the database for testing.

insert into demo.test_data(id, name, test_items, myblob,mybool, myfloat)
    values(UUID(), 'Name One', 
        [{record_id: UUID(), quantity: 4, name: 'Widget'}], 
        textAsBlob('bdb14fbe076f6b94444c660e36a400151f26fc6f'), TRUE, 39.65
);

insert into demo.test_data(id, name, test_items, myblob,mybool, myfloat)
    values(UUID(), 'Name Two', 
        [{record_id: UUID(), quantity: 4, name: 'Gizmo'}], 
        textAsBlob('bdb14fbe076f6b94444c660e36a400151f26fc6fdsfioioqgoiqgioeugioqeuiogueiguqeoiguoeiqguoieugoieugoieugoieugoieugiowuoiguwoiguwoiguwoiugiowugoiewug
        ergqeroigqeiorguioqeugoiqeugoierugweroiguweoirugowiugiouioeruqioeruoieqrutiore'), TRUE, 39.65
);
