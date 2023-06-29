import { rest } from "msw";

export const handlers = [
	// Handles a POST /login request
	rest.post("http://127.0.0.1:5173/api/login", (req, res, ctx) => {
		return res(
			// Respond with a 200 status code
			ctx.status(200)
		);
	}),
];
