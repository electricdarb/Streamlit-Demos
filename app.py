import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def main():
    st.markdown(
        """
    # Casey's example 

    an example brad is writing for casey 
    """
    )

    # split into left and right cols
    left, right = st.columns(2)

    x = np.linspace(0, 7, 100)
    y = np.sin(x)

    # create fig and axis to plot on
    fig, ax = plt.subplots()

    # plot values
    ax.plot(x, y)
    left.write(fig)

    with right:
        st.markdown(
            """
        This is the right columns, to the left is a sin wave
        """
        )

        st.bar_chart(
            {"x": [1, 2, 3], "y": [2, 3, 4]},
        )


if __name__ == "__main__":
    main()
