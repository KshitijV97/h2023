import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import App from "./App.tsx";
import "./index.css";

import { setupWorker } from "msw";
import { handlers } from "./mocks/handlers";

// This configures a Service Worker with the given request handlers.
export const worker = setupWorker(...handlers);

if (process.env.NODE_ENV === "development") {
	// eslint-disable-next-line @typescript-eslint/no-var-requires
	worker.start();
}

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
	<React.StrictMode>
		<BrowserRouter>
			<App />
		</BrowserRouter>
	</React.StrictMode>
);
