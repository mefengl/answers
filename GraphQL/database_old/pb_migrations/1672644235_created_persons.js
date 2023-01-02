migrate((db) => {
  const collection = new Collection({
    "id": "3doh6uvwfx4rzz0",
    "created": "2023-01-02 07:23:55.696Z",
    "updated": "2023-01-02 07:23:55.696Z",
    "name": "persons",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "dbpzcqz4",
        "name": "name",
        "type": "text",
        "required": true,
        "unique": true,
        "options": {
          "min": 6,
          "max": 18,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "frfdksma",
        "name": "phone",
        "type": "number",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null
        }
      },
      {
        "system": false,
        "id": "xytgjdee",
        "name": "street",
        "type": "text",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "ubjyixic",
        "name": "city",
        "type": "text",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      }
    ],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("3doh6uvwfx4rzz0");

  return dao.deleteCollection(collection);
})
