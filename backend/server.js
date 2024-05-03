import express from "express";
import mongoose from "mongoose";
import cors from "cors";
import router from "./routes/router.js";

const app = express();

const connect = async () => {
  try {
    await mongoose.connect("mongodb://127.0.0.1:27017/level");
    console.log("Mongodb Connected..");
  } catch (error) {
    throw error;
  }
};

mongoose.connection.on("connected", () => {
  console.log("Connected to MongoDB!");
});

mongoose.connection.on("disconnected", () => {
  console.log("Mongodb disconnected...");
});

app.use(express.json());
app.use(cors());
app.use("/backend", router);

app.listen(4000, () => {
  connect();
  console.log("Server Started..");
});
