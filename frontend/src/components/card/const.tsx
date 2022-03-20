import { faArrowAltCircleUp, faFire, faSun } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { ReactNode } from "react";

const styles = {
    iconPadding: "ms-2",
};

const sortMethodMap: { [s: string]: ReactNode } = {
    hot: (
        <>
            Hot <FontAwesomeIcon icon={faFire} className={styles.iconPadding} />
        </>
    ),
    best: (
        <>
            Best <FontAwesomeIcon icon={faArrowAltCircleUp} className={styles.iconPadding} />
        </>
    ),
    new: (
        <>
            New <FontAwesomeIcon icon={faSun} className={styles.iconPadding} />
        </>
    ),
};
export const sortMethods = Object.keys(sortMethodMap);
export const sortMethodItems = Object.entries(sortMethodMap);
export const listColumns = 1;
