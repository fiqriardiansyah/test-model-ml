const express = require("express");
const axios = require("axios");
const app = express();

app.use(express.json());

app.post("/translate", async (req, res) => {
  try {
    const { text } = req.body;

    // Call Python model API
    const response = await axios.post("http://127.0.0.1:5005/translate", {
      text,
    });

    res.json(response.data);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Model error" });
  }
});

app.listen(3000, () => console.log("Express running on http://localhost:3000"));
