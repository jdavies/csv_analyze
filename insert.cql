# Insert.cql
#
# By: Jeff Davies
#
# Create some data in the database for testing.

insert into demo.test_data(id, name, test_items, myblob,mybool, myfloat)
    values(UUID(), 'Name One', 
        [{record_id: UUID(), quantity: 4, name: 'Widget'}], 
        textAsBlob('bdb14fbe076f6b94444c660e36a400151f26fc6f'), TRUE, 1.65
);

insert into demo.test_data(id, name, test_items, myblob,mybool, myfloat)
    values(UUID(), 'Name Two', 
        [{record_id: UUID(), quantity: 4, name: 'Gizmo'}], 
        textAsBlob('bdb14fbe076f6b94444c660e36a400151f26fc6fdsfioioqgoiqgioeugioqeuiogueiguqeoiguoeiqguoieugoieugoieugoieugoieugiowuoiguwoiguwoiguwoiugiowugoiewug
        ergqeroigqeiorguioqeugoiqeugoierugweroiguweoirugowiugiouioeruqioeruoieqrutiore'), TRUE, 39.65
);

insert into demo.test_data(id, name, test_items, myblob,mybool, myfloat)
    values(UUID(), 'Name Three', 
        [{record_id: UUID(), quantity: 4, name: 'Widget'},
        {record_id: UUID(), quantity: 4, name: 'Gizmo'},
        {record_id: UUID(), quantity: 4, name: 'Whatsit'}], 
        textAsBlob('bdb14fbe076f6b94444c660e36a400151f26fc6fdsfioioqgoiqgioeugioqeuiogueiguqeoiguoeiqguoieugoieugoieugoieugoieugiowuoiguwoiguwoiguwoiugiowugoiewug
        ergqeroigqeiorguioqeugoiqeugoierugweroiguweoirugo1434iot3rh3130iig04rt904u4rjgio4j24j2450j045j09245y24059ywiugiouioeruqioeruoieqrutiore'), 
        TRUE, 139.65
);


#
# Data witout the Blob
#
insert into demo.test_data(id, name, mybool, myfloat)
    values(UUID(), 'Name One', TRUE, 39.65
);

insert into demo.test_data(id, name, mybool, myfloat)
    values(UUID(), 'Name Two', TRUE, 39.65
);

insert into demo.test_data(id, name, mybool, myfloat)
    values(UUID(), 'Name Three', TRUE, 39.65
);