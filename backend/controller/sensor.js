import mongoose from "mongoose";
import asset from "../model/asset.js";

export const createAsset = async (req, res) => {
    const {
        id,
        level,
        devicetemp,
        signal,
        batterylevel,
        humidity,
        pressure,
        altitude,
        datafrequency
    } = req.query;

    const saveAsset = new asset({
        id: String(id),
        level: String(level),
        devicetemp: String(devicetemp),
        signal: String(signal),
        batterylevel: String(batterylevel),
        humidity: String(humidity),
        pressure: String(pressure),
        altitude: String(altitude),
        datafrequency: String(datafrequency)
    });

    try {
        const savedAsset = await saveAsset.save();
        res.status(200).json(savedAsset);
    } catch (error) {
        res.status(500).json({
            message: error.message
        });
    }
};