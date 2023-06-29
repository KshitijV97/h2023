import { createTheme } from "@mui/material/styles";

// Create a theme instance.
const theme = createTheme({
	palette: {
		type: "dark", // Set the theme type to dark
		primary: {
			main: "#2196f3", // A vibrant blue color for primary elements
		},
		secondary: {
			main: "#f50057", // A vivid pink color for secondary elements
		},
		background: {
			default: "#121212", // Dark background color
			paper: "#212121", // Gray color for paper-based elements
		},
		text: {
			primary: "#ffffff", // White color for primary text
			secondary: "#cccccc", // Light gray color for secondary text
		},
	},
	typography: {
		fontFamily: ["Roboto", "Arial", "sans-serif"].join(","),
		fontSize: 16,
		fontWeightLight: 300,
		fontWeightRegular: 400,
		fontWeightMedium: 500,
		fontWeightBold: 700,
	},
	shape: {
		borderRadius: 8, // Rounded corners for elements
	},
});

export default theme;
