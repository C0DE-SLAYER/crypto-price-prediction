const mongoose = require("mongoose");

const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  passw: String,
});

module.exports = mongoose.model("signupto", userSchema);
