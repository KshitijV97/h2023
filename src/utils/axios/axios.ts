import axios, {
	AxiosInstance,
	InternalAxiosRequestConfig,
	AxiosRequestConfig,
	AxiosResponse,
	AxiosError,
} from "axios";

export const axiosInstance: AxiosInstance = axios.create({
	baseURL: "",
	timeout: 5000,
	headers: {
		"Content-Type": "application/json",
		Authorization: "Bearer token123",
	},
	withCredentials: true,
});

// Add a request interceptor
axiosInstance.interceptors.request.use(
	function (config: InternalAxiosRequestConfig): InternalAxiosRequestConfig {
		// Do something before request is sent
		return config;
	},
	function (error: AxiosError): Promise<AxiosError> {
		// Do something with request error
		return Promise.reject(error);
	}
);

// Add a response interceptor
axiosInstance.interceptors.response.use(
	function (response: AxiosResponse): AxiosResponse {
		// Any status code that lie within the range of 2xx cause this function to trigger
		// Do something with response data
		return response;
	},
	function (error: AxiosError): Promise<AxiosError> {
		// Any status codes that falls outside the range of 2xx cause this function to trigger
		// Do something with response error
		return Promise.reject(error);
	}
);
