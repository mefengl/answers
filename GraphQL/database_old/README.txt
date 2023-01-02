https://pocketbase.io/docs/

./pocketbase serve

http://127.0.0.1:8090/_/


npm i pocketbase

import PocketBase from 'pocketbase';
const pb = new PocketBase('http://127.0.0.1:8090');

const records = await pb.collection('persons').getFullList();
const record = await pb.collection('persons').getOne('RECORD_ID');
const record = await pb.collection('persons').create({ name: 'John Doe'});
const record = await pb.collection('persons').update({ 'RECORD_ID', { name: 'John Doe' }});
const record = await pb.collection('persons').delete('RECORD_ID');
