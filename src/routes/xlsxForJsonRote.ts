import express from 'express'
import cors from 'cors' 
import multer from 'multer';
import { xlsxForJsonController } from '../controllers/xlsxForJsonController';

const router = express.Router();
const app = express();

app.use(express.json())
app.use(cors())

// configuração do multer para tratar de arquivos
const upload = multer({
    dest: 'upload/', //pasta temporária para salvar arquivos
});

router.post('/', upload.single('arquivo'), async (req, res, next) => {
    xlsxForJsonController(req, res).catch(next)
})


export  default router