import { useState } from "react";
import { FontAwesomeIcon as FaIcon } from "@fortawesome/react-fontawesome";
import {
    faArrowUp,
    faArrowDown,
    IconDefinition,
} from "@fortawesome/free-solid-svg-icons";
import { Components } from "types/apiclient";
import { useAuth } from "../../context/auth";

type BingoCard = Components.Schemas.CardListSchema | Components.Schemas.CardDetailSchema;
interface VoteButtonSingleProps {
    icon: IconDefinition;
    color: string;
    voteAction: () => void;
}

interface VoteButtonsProps {
    card: BingoCard;
    itemMargin?: string;
}

type Upvote = boolean | null;

const styles = {
    color: {
        //upvote: "text-sdark-orange",
        //downvote: "text-sdark-violet",
        //novote: "text-sdark-fg",
        upvote: "text-warning",
        downvote: "text-primary",
        novote: "text-muted",
    },
    margin: {
        score: "m-0",
    },
    align: {
        vote: "w-100 text-center",
    },
    voteButton: "vote-btn p-1 rounded",
};

function VoteButtonSingle({ icon, color, voteAction }: VoteButtonSingleProps) {
    const { doIfAuth } = useAuth();

    return (
        <div
            className={`${color}`}
            onClick={() => doIfAuth(voteAction)}
            style={{ cursor: "pointer" }}
        >
            <FaIcon icon={icon} />
        </div>
    );
}

export default function VoteButtons({ card, itemMargin = "" }: VoteButtonsProps) {
    const [upvoted, setUpvoted] = useState<Upvote>(
        card.is_upvoted === undefined ? null : card.is_upvoted
    );
    const { getClient } = useAuth();

    let upColor, downColor, scoreColor;
    upColor = downColor = scoreColor = styles.color.novote;

    switch (upvoted) {
        case true:
            upColor = scoreColor = styles.color.upvote;
            break;
        case false:
            downColor = scoreColor = styles.color.downvote;
            break;

        default:
    }

    const upvoteScore = (vote: Upvote) => (vote === null ? 0 : vote ? 1 : -1);
    const scoreAdjust =
        upvoteScore(upvoted) -
        upvoteScore(card.is_upvoted === undefined ? null : card.is_upvoted);

    const voteAction = async (up: boolean) => {
        setUpvoted(upvoted === null || up !== upvoted ? up : null);
        const client = await getClient();
        await client.vote_card(null, { card_id: card.id, up: up });
    };

    return (
        <div className={styles.align.vote}>
            <div className={itemMargin}>
                <VoteButtonSingle
                    icon={faArrowUp}
                    color={upColor}
                    voteAction={() => voteAction(true)}
                />
            </div>
            <div className={`${scoreColor} ${itemMargin}`}>
                <h5 className={styles.margin.score}>{card.score + scoreAdjust}</h5>
            </div>
            <div className={itemMargin}>
                <VoteButtonSingle
                    icon={faArrowDown}
                    color={downColor}
                    voteAction={() => voteAction(false)}
                />
            </div>
        </div>
    );
}
