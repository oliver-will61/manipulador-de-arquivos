import app from './app'
import dotenv from 'dotenv'

dotenv.config()

const PORT: string = String(process.env.PORT) 
const HOST: string = String(process.env.HOST)

app.listen(PORT, () => {
    console.log(`Servidor rodando em ${HOST}: ${PORT}`)
})
