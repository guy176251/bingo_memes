import { Link } from "react-router-dom";

export default function titleWithHashtags(cardTitle: string) {
    let hashtagRe = /(#\w+)/g;
    let matches = [...cardTitle.matchAll(hashtagRe)];
    let matchStrs = matches.map((m) => m[1]);
    let tokens = cardTitle.split(hashtagRe);
    return tokens.map((t) =>
        matchStrs.includes(t) ? <Link to={`/hashtags/${t.slice(1)}`}>{t}</Link> : t
    );
}

const monthNames = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
];

const timeUnits = (() => {
    const minute = 1000 * 60;
    const hour = minute * 60;
    const day = hour * 24;
    const month = day * 31;
    const year = month * 12;

    return {
        minute,
        hour,
        day,
        month,
        year,
    };
})();

// from big to small
const orderedTimeUnits: { [s: string]: number } = {
    h: timeUnits.hour,
    m: timeUnits.minute,
};

const orderdTimeItems = Object.entries(orderedTimeUnits);

export const createdAtStr = (isoString: string) => {
    const now = new Date();
    const date = new Date(Date.parse(isoString));
    const diff = now.getTime() - date.getTime();

    if (diff >= timeUnits.day) {
        const yearString =
            date.getFullYear() !== now.getFullYear() ? `, ${date.getFullYear()}` : "";

        return `${monthNames[date.getMonth()]} ${date.getDate()}${yearString}`;
    }

    for (const [label, unit] of orderdTimeItems) {
        if (diff >= unit) {
            let value = Math.floor(diff / unit);
            value = unit === timeUnits.minute ? value % 60 : value;
            return `${value}${label}`;
        }
    }

    return "just now";
};
