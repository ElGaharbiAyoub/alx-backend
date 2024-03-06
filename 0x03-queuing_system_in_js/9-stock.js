import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

const client = createClient();

client.on('connect', function () {
  console.log('Redis client connected to the server');
});

client.on('error', function (err) {
  console.log(`Redis client not connected to the server: ${err}`);
});

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}

function reserveStockById(itemId, stock) {
  client.set(itemId, stock);
}

async function getCurrentReservedStockById(itemid) {
  const getAsync = promisify(client.get).bind(client);
  const reservedStock = await getAsync(itemid);
  return reservedStock;
}

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);
  if (item === undefined) {
    res.status(404).json({ status: 'Product not found' });
  } else {
    const reservedStock = await getCurrentReservedStockById(itemId);
    if (reservedStock === null) {
      item.reservedStock = 0;
    } else {
      item.reservedStock = reservedStock;
    }
    item.currentQuantity = item.stock - item.reservedStock;
    res.json(item);
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);
  if (item === undefined) {
    res.status(404).json({ status: 'Product not found' });
  } else if (item.stock === 0) {
    res.status(400).json({ status: 'Not enough stock available', itemId });
  } else {
    const reservedStock = await getCurrentReservedStockById(itemId);
    if (reservedStock === null) {
      reserveStockById(itemId, 1);
    } else {
      reserveStockById(itemId, parseInt(reservedStock, 10) + 1);
    }
    res.json({ status: 'Reservation confirmed', itemId: itemId });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
