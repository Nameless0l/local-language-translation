export default function LanguageSelector({ text, value, setValueCallback, isTranlating, languages }) {

    return (

        <div className="col-lg-6">

            <div className="chat-about">
                <div className="form-group">
                    <label htmlFor="exampleFormControlSelect1"><h6>{text}</h6></label><br />
                    <select className="form-select form-select-sm" id="exampleFormControlSelect1" disabled={isTranlating} value={value} onChange={(e) => { setValueCallback(e.target.value) }}>
                        {
                            Object.keys(languages).map((key) =>
                                (<option key={key} value={key}>{languages[key]}</option>))
                        }
                    </select>
                </div>
            </div>

        </div>


    );
}