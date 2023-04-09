export default function outputMessage({output, final}){
    return ( <li className="clearfix">
    <div className="message-data">
        <span className="message-data-time">{final}</span>
    </div>
    <div className="message my-message">{output}</div>
</li>
)
}