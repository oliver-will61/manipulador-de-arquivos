
import { Request, Response } from 'express'; // ← Importe do Express
import { PythonService } from '../services/PyhonService';


export const xlsxForJsonController = async (req: Request, res: Response) => {
    try {    

        if (!req.file) {
            return res.status(400).json({
                mensagem: "Nenhum arquivo enviado"
            })
        }

        console.log("Enviando para a API do Python...");

        const pythonService = new PythonService
        pythonService.enviarParaPython(req, res)        
    }

    catch (error) {
        console.error("Erro no arquivo", error)

        return res.status(500).json({
            mensagem:"Erro no servidor",
            error: error 
        })
    }
}
    

