import { useEffect, useState } from 'react'
import './assets/styles/chat.css'
import InputComponent from './components/InputComponent'
import InputMessage from './components/InputMessage'
import OutputMessage from './components/OutputMessage'
import ApiClient from './api/Requests'
import { toast } from 'react-toastify'
import LanguageSelector from './components/LanguageSelector'

export default function Chat() {
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

    useEffect(() => {
        if (!playedOnce) {
            apiClient.getLanguages().then(langs => {
                setInitial(Object.keys(langs)[0])
                setFinal(Object.keys(langs)[1])
                setLanguages(langs)
            })


            setPlayedOnce(true)
        }

    }, [output])

    const apiClient = new ApiClient()

    const translate = () => {
        let hasError = false
        setIsTranslating(true)
        if (initial == final) {
            toast("The input language has to be different from the output language", { type: 'error' })
            hasError = true
        }
        if (input.trim() === "") {
            toast('You have to enter a text in the in put zone', { type: "warning" })
            hasError = true
        }

        if (!hasError)
            apiClient.translate(initial, final, input).then(translation => {
                setOutput(translation.output);
                setHistory((previous) => [...(previous), { initial, final, input, output }])
                toast('Translated with success', { type: 'success' })
            })
        setIsTranslating(false)

    }

    return (
        <div className="container">
            <div className="row clearfix">
                <div className="col-lg-12">
                    <div className="card chat-app">

                        <div className="chat">
                            <div className="chat-header clearfix">
                                <div className="row">

                                    <LanguageSelector text="Output Language " value={final} languages={languages} isTranlating={isTranslating} setValueCallback={(value) => setFinal(value)} />
                                    <LanguageSelector text="Input Language " value={initial} languages={languages} isTranlating={isTranslating} setValueCallback={(value) => setInitial(value)} />

                                </div>
                            </div>
                            <div className="chat-history">
                                <ul className="m-b-0">


                                    {
                                        history.length == 0 ?
                                            "No translation generated. Select an input language and an output language, enter your text and send it ..."
                                            :
                                            history.map((e, index) => (
                                                <div key={index}>
                                                    <InputMessage input={e.input} initial={languages[e.initial]} />
                                                    <OutputMessage output={e.output} final={languages[e.final]} />
                                                </div>
                                            ))


                                    }
                                </ul>
                            </div>
                            <InputComponent translateCallback={translate} isTranslating={isTranslating} setInputCallBack={(input) => setInput(input)} inputValue={input} />
                        </div>
                    </div>
                </div>
            </div>
        </div>)
}