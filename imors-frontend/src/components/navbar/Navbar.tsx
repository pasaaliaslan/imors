import React, { useEffect, useState } from "react";
import { User } from "../../models/types";
import "./Navbar.scss";

export const Navbar = (): React.ReactElement => {
    const [profile, setProfile] = useState<User>();

    const hasProfile = () => {
        return profile != null;
    };

    useEffect(() => {
        // Checking token goes here
        // Sayfaya bak. Homepage degilse ve profil yoksa, homepage isinla.
    }, []);

    return (
        <div id="navbar">
            <div className="logo">
                <img src="/logo.png" />
                <h1>imörs</h1>
            </div>
            {hasProfile() ? (
                <div className="right-navbar">
                    {profile?.email} | {profile?.username}
                </div>
            ) : (
                <div className="right-navbar">Login</div>
            )}
        </div>
    );
};
