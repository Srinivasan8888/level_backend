import express from 'express';
import {createAsset } from '../controller/sensor.js'

const router = express.Router();

router.get('/insert', createAsset);



export default router;