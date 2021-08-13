        df2.index = df1.index

        total_df = pd.concat([df1, df2], axis=1)
        total_df.plot()
        plt.show()