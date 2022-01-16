import { TestHome, TestChild } from "../layouts/test";
import { RouteObject } from "react-router-dom";

export const ROUTES: RouteObject[] = [
    {
        path: "/",
        element: <TestHome />,
        children: [
            { path: "home", index: true, element: <TestChild /> },
            {
                path: "one",
                element: <TestChild name="one" />,
                children: [{ path: "nested", element: <TestChild name="nested_one" /> }],
            },
            { path: "two", element: <TestChild name="two" /> },
            { path: "three", element: <TestChild name="three" /> },
            { path: "*", element: <h1>Not Found</h1> },
        ],
    },
];
