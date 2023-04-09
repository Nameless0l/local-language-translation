
import axios from "axios";
export default class ApiClient{
    constructor(apiBaseUrl = "http://localhost:8000"){
        this.apiBaseUrl = apiBaseUrl
    }
    async getLanguages(){
        const response  = await axios.get(`${this.apiBaseUrl}/languages`).then(res=>res.data).catch(err=>err)
        return response
    }

    async translate(initial, final, input){
        const response = await 
        axios.post(`${this.apiBaseUrl}/translate`, 
        {
            "initial":initial,"final": final,"input": input,
        }).then(res=>res.data).catch(err=> err)

        return response;
    }
}