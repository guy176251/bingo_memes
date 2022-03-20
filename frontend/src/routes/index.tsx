import CardPlaceholderComponent from "components/card/placeholder";
import MainLayout from "layouts";
import CardDetailLayout from "layouts/carddetail";
import CardListLayout from "layouts/cardlist";
import { RouteObject } from "react-router-dom";
import {
    TestCardDetailLayout,
    TestCardMainLayout,
    TestChild,
    TestHome,
} from "../layouts/test";

export const ROUTES: RouteObject[] = [
    {
        path: "/",
        element: <MainLayout />,
        children: [
            {
                path: "cards",
                element: <CardListLayout />,
            },
            {
                path: "cards/:cardId",
                element: <CardDetailLayout />,
            },
            {
                path: "*",
                element: (
                    <div className="text-center my-3">
                        <h1>Not Found</h1>
                    </div>
                ),
            },
        ],
    },
    {
        path: "/test",
        element: <TestHome />,
        children: [
            { path: "home", index: true, element: <TestChild /> },
            {
                path: "card",
                element: <TestCardMainLayout />,
                children: [
                    {
                        path: ":cardId",
                        element: <TestCardDetailLayout />,
                    },
                ],
            },
            {
                path: "one",
                element: <TestChild name="one" />,
                children: [{ path: "nested", element: <TestChild name="nested_one" /> }],
            },
            { path: "two", element: <TestChild name="two" /> },
            { path: "three", element: <TestChild name="three" /> },
            { path: "placeholder", element: <CardPlaceholderComponent /> },
            { path: "*", element: <h1>Not Found</h1> },
        ],
    },
];
