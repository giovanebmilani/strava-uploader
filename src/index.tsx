import ReactDOM from "react-dom";
import { AuthProvider } from "./providers/auth/AuthProvider";

import { AppRoutes } from "./routes/AppRoutes";

ReactDOM.render(
  <AuthProvider>
    <AppRoutes />
  </AuthProvider>,
  document.getElementById("root")
)
