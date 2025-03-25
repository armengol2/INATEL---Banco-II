{
    $jsonSchema: {
      bsonType: 'object',
      required: [
        '_id',
        'titulo',
        'autor',
        'ano',
        'preco'
      ],
      properties: {
        _id: {
          bsonType: 'objectId',
          description: 'O ID deve ser um número inteiro.'
        },
        titulo: {
          bsonType: 'string',
          minLength: 1,
          description: 'O título deve ser uma string não vazia.'
        },
        autor: {
          bsonType: 'string',
          minLength: 1,
          description: 'O autor deve ser uma string não vazia.'
        },
        ano: {
          bsonType: 'int',
          minimum: 1000,
          maximum: 2025,
          description: 'O ano deve ser um número inteiro entre 1000 e 2025.'
        },
        preco: {
          bsonType: 'double',
          minimum: 0,
          description: 'O preço deve ser um número decimal positivo.'
        }
      }
    }
  }