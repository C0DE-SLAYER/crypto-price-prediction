const express = require("express");
const cors = require("cors");
require("./db/config");
const Signup = require("./db/Signup");
const { response } = require("express");
const app = express();

app.use(express.json());
app.use(cors());

app.post("/register", async (req, res) => {
  let Signup1 = new Signup(req.body);
  let result = await Signup1.save();
  res.send(result);
});

app.post("/login", async (req, res) => {
  console.log(req.body);
  if (req.body.passwe && req.body.namee) {
    let signup2 = await Signup.findOne({ name: req.body.namee });
    if (signup2) {
      res.send(signup2);
    } else {
      res.send({ result: "no user found" });
    }
  } else {
    res.send({ result: "no user found" });
  }
});

app.listen(5000);
