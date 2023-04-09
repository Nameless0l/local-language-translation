export default function InputMessage({ input, initial }) {
    return (
        <li className="clearfix">
            <div className="message-data text-end">
                <span className="message-data-time text-right">{initial}</span>
            </div>
            <div className="message other-message float-right"> {input}</div>

        </li>
    )
}