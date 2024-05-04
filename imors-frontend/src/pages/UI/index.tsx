import React from "react";
import Button from "../../components/UI/Button";

export default function UI() {
    return (
        <div>
            {["small", "medium", "large"]
                .map((size) => {
                    return ["primary", "secondary", "link", "disabled"].map((variant) => {
                        return (
                            <Button key={`${size}-${variant}`} size={size} variant={variant}>
                                Click
                            </Button>
                        );
                    });
                })
                .flat()}
        </div>
    );
}
