import { useEffect, useState } from 'react'
import ApiClient from './api/Requests'
import LanguageSelector from "./components/LanguageSelector"
import InputComponent from './components/InputComponent'
import OutputComponent from './components/OutputComponent'
import { toast } from 'react-toastify'
export default function App() {
  //Langues disponibles dans l'application
  const [languages, setLanguages] = useState({})

  //parametres pour la traduction
  const [initial, setInitial] = useState("") //langue de depart
  const [final, setFinal] = useState("")//langue d'arrivée
  const [input, setInput] = useState("")//le texte en entrée à traduire
  const [output, setOutput] = useState("") // le texte en sorti un fois traduit
  const [history, setHistory] = useState([]) //L'historique des traductions

  const [playedOnce, setPlayedOnce] = useState(false)
  const [isTranslating, setIsTranslating] = useState(false)

  useEffect(()=>{
    if(!playedOnce){
      apiClient.getLanguages().then(langs=> {
        setInitial(Object.keys(langs)[0])
        setFinal(Object.keys(langs)[1])
        setLanguages(langs)})

      
      setPlayedOnce(true)
    }
    setHistory((previous) => [...previous, {initial, final, input, output}])
    console.log(history)
  }, [output])

  const apiClient = new ApiClient()

  const translate = ()=>{
    let hasError = false
    setIsTranslating(true)
    if(initial == final ){
      toast("The input language has to be different from the output language", {type:'error'})
      hasError = true
    }
    if(input.trim() === "" ){
      toast('You have to enter a text in the in put zone', {type: "warning"})
      hasError = true
    }
    
    if(!hasError)
    apiClient.translate(initial, final, input).then(translation=>{
      setOutput(translation.output)
      toast('Translated with success',{type:'success'})
    })
    setIsTranslating(false)

  }
  
  
  
  return (
    <div className="App">
      <LanguageSelector text="From " value={initial} languages={languages} isTranlating={isTranslating} setValueCallback={(value)=>setInitial(value)}/>
      <LanguageSelector text="To " value={final} languages={languages} isTranlating={isTranslating} setValueCallback={(value)=>setFinal(value)}/>
      <InputComponent isTranslating={isTranslating} setInputCallBack={(input)=>setInput(input)} inputValue={input}  />
      <OutputComponent outputValue={output}/>
      <div className="btn btn-outline-primary" onClick={translate}>
        Translate
      </div>
    </div>
  )
}



