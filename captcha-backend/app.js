const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.post('/verify-motion', (req, res) => {
  const { acceleration, rotationRate } = req.body;

  // ML model logic to determine if the motion is human-like
  // Placeholder logic: if motion is above a certain threshold
  if (Math.abs(acceleration.x) > 2 || Math.abs(acceleration.y) > 2 || Math.abs(acceleration.z) > 2) {
    return res.json({ message: 'You are human!' });
  } else {
    return res.json({ message: 'You are a bot!' });
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
