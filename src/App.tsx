import "./App.css";
import { Routes, Route, useLocation } from "react-router-dom";
import { NotFound } from "./pages/NotFound";
import { BookRoutes } from "./routes/BookRoutes";
import { ZustandExample } from "./pages/ZustandExample/ZustandExample";

import CssBaseline from "@mui/material/CssBaseline";
import { ThemeProvider } from "@mui/material/styles";
import SignInSide from "./pages/SignInSide/SignInSide";
import Dashboard from "./pages/DashboardNew/Dashboard";
import Sidebar from "./pages/global/Sidebar";
import Topbar from "./pages/global/Topbar";
import { useState } from "react";
import { ColorModeContext, useMode } from "./theme";

function App() {
  const [theme, colorMode] = useMode();
  const location = useLocation();
  const [isSidebar, setIsSidebar] = useState(true);
  console.log("this is setIsSidebar", isSidebar);
  //   const showNav: boolean = location.pathname === "/";
  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="app">
          <Sidebar isSidebar={isSidebar} />
          <main className="content">
            <Topbar setIsSidebar={setIsSidebar} />
            <Routes>
              <Route path="/" element={<SignInSide />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/books" element={<BookRoutes />} />
              <Route path="/zustand-example" element={<ZustandExample />} />
              <Route path="*" element={<NotFound />} />
              {/* <Route path="/team" element={<Team />} /> */}
              {/* <Route path="/contacts" element={<Contacts />} /> */}
              {/* <Route path="/invoices" element={<Invoices />} /> */}
              {/* <Route path="/form" element={<Form />} /> */}
              {/* <Route path="/bar" element={<Bar />} /> */}
              {/* <Route path="/pie" element={<Pie />} /> */}
              {/* <Route path="/line" element={<Line />} /> */}
              {/* <Route path="/faq" element={<FAQ />} /> */}
              {/* <Route path="/calendar" element={<Calendar />} /> */}
              {/* <Route path="/geography" element={<Geography />} /> */}
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
