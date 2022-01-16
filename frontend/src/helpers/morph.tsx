import { Link } from "react-router-dom";

function cardNameHashtags(cardName: string) {
    let hashtagRe = /(#\w+)/g;
    let matches = [...cardName.matchAll(hashtagRe)];
    let matchStrs = matches.map((m) => m[1]);
    let tokens = cardName.split(hashtagRe);
    return tokens.map((t) => (matchStrs.includes(t) ? "REPLACED" : t));
}
