migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("3doh6uvwfx4rzz0")

  collection.listRule = ""
  collection.viewRule = ""

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("3doh6uvwfx4rzz0")

  collection.listRule = null
  collection.viewRule = null

  return dao.saveCollection(collection)
})
