import express from 'express'
import cors from 'cors' 
import xlsxForJsonRota from './routes/xlsxForJsonRote'

const app = express()

app.use(express.json());
app.use(cors())

app.use('/xlsx-json', xlsxForJsonRota)

export default app

