import { useState } from "react";
import { FontAwesomeIcon as FaIcon } from "@fortawesome/react-fontawesome";
import {
    faArrowUp,
    faArrowDown,
    IconDefinition,
} from "@fortawesome/free-solid-svg-icons";
import { Components } from "../../api/client";
import { getAPIClient } from "../../api/axios";

interface VoteButtonSingleProps {
    icon: IconDefinition;
    color: string;
    voteAction: () => void;
}

interface VoteButtonsProps {
    card: Components.Schemas.CardOutSchema;
    itemMargin?: string;
}

type Upvote = boolean | null;

const styles = {
    color: {
        upvote: "text-sdark-orange",
        downvote: "text-sdark-violet",
        novote: "text-sdark-fg",
    },
    margin: {
        score: "m-0",
    },
    voteButton: "vote-btn p-1 rounded",
};

const VoteButtonSingle = ({ icon, color, voteAction }: VoteButtonSingleProps) => {
    const { ifAuth } = useAuth();

    return (
        <div
            className={`${color} ${styles.voteButton}`}
            onClick={() => ifAuth(voteAction)}
        >
            <FaIcon icon={icon} />
        </div>
    );
};

const VoteButtons = ({ card, itemMargin = "" }: VoteButtonsProps) => {
    const [upvoted, setUpvoted] = useState<Upvote>(card.upvoted || null);

    /*
    const upColor = upvoted ? styles.color.upvote : styles.color.novote;
    const downColor = upvoted === false ? styles.color.downvote : styles.color.novote;
    const scoreColor = upvoted === null ? "fg" : upvoted ? "orange" : "violet";
     */

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
    const scoreAdjust = upvoteScore(upvoted) - upvoteScore(card.upvoted || null);

    const voteAction = async (up: boolean) => {
        setUpvoted(upvoted === null || up !== upvoted ? up : null);
        const client = await getAPIClient();
        await client.card_api_create_vote(null, { card_id: card.id, up: up });
    };

    return (
        <>
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
        </>
    );
};
