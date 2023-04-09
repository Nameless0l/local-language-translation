export default function InputComponent({ isTranslating, inputValue, setInputCallBack, translateCallback }) {

    return (
        <div className="chat-message clearfix">
                            
            <div className="input-group mb-0">
                <div className="input-group-prepend" onClick={(e) => translateCallback()}>
                    <span className="input-group-text"><i className="fa fa-send"></i></span>
                </div>
                <input disabled={isTranslating} value={inputValue} placeholder="Your text here ...." onChange={(e) => setInputCallBack(e.target.value)} type="text" className="form-control" />
            </div>
        </div>
    )

}